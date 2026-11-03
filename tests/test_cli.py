import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from dsg_project.cli import summarize


class CsvTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "input.csv"

    def write(self, contents):
        self.path.write_text(contents, encoding="utf-8")
        return self.path

    def test_counts_records_including_quoted_multiline_fields(self):
        result = summarize(self.write('name,value\n"two\nlines",1\n\nother,2\n'))
        self.assertEqual(result, {"columns": ["name", "value"], "rows": 2})

    def test_header_only_and_bom(self):
        self.assertEqual(summarize(self.write('\ufeffname,value\n'))["rows"], 0)

    def test_rejects_missing_or_duplicate_headers(self):
        for value in ('', '\n', 'name,\n', 'name,   \n', 'name,name\n'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                summarize(self.write(value))

    def test_rejects_wrong_record_width(self):
        for value in ('name,value\nonlyone\n', 'name,value\na,b,c\n'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                summarize(self.write(value))

    def test_cli_outputs_json_without_row_values(self):
        self.write('name,value\nprivate-example,1\n')
        result = subprocess.run(
            [sys.executable, '-m', 'dsg_project.cli', str(self.path)],
            capture_output=True, text=True, check=True,
        )
        self.assertEqual(json.loads(result.stdout), {"columns": ["name", "value"], "rows": 1})
        self.assertNotIn('private-example', result.stdout)

    def test_installed_command(self):
        executable = shutil.which('dsg-project')
        self.assertIsNotNone(executable, 'Install the package before running tests')
        self.write('name,value\nalpha,1\nbeta,2\n')
        result = subprocess.run(
            [executable, str(self.path)], capture_output=True, text=True, check=True,
        )
        self.assertEqual(
            json.loads(result.stdout), {"columns": ["name", "value"], "rows": 2},
        )

    def test_cli_reports_missing_and_invalid_files(self):
        for contents in (None, 'name,name\n'):
            if contents is not None:
                self.write(contents)
            result = subprocess.run(
                [sys.executable, '-m', 'dsg_project.cli', str(self.path)],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn('error:', result.stderr)
            self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
