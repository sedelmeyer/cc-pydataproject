import contextlib
import os
from pathlib import Path
import tempfile
from unittest import TestCase

from cookiecutter import main


#: Define absolute path to cc-pydata cookiecutter project directory
CCDIR = Path(__file__).resolve().parents[1]


#: Define list of top-level files expected in built template
template_files = [

]


#: Define list of sub-directories expected in built template
template_directories = [

]


class TestBuildTemplate(TestCase):
    """Test default cookiecutter template build"""

    def setUp(self):
        """Build template in temporary directory"""
        with contextlib.ExitStack() as stack:
            # open temp directory context manager
            self.tmpdir = tmpdir = stack.enter_context(
                tempfile.TemporaryDirectory()
            )
            # build cookie template in temp directory
            main.cookiecutter(
                template=str(CCDIR),
                no_input=True,
                extra_context=None,
                output_dir=tmpdir
            )
            # get path to built template directory
            self.builtdir = Path(tmpdir).resolve() / 'project_name'
            # ensure context manager closes after tests
            self.addCleanup(stack.pop_all().close)

    def test_project_exists(self):
        """Ensure built template exists in temp dir"""
        self.assertTrue(os.path.isdir(self.builtdir))

    def test_unfilled_brackets(self):
        """Ensure no curly brackets are left over from jinja build"""
        raise NotImplementedError

    def test_files_exist():
        """Ensure top-level files exist"""
        raise NotImplementedError

    def test_subdirs_exist():
        """Ensure top-level sub-directories exist"""
        raise NotImplementedError
