CALL conda activate.bat mybuild
echo "hello" %CONDA_PREFIX%
python -m pytest --verbose --junit-xml reports/unit_tests.xml
