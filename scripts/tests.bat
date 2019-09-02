CALL conda.bat activate mybuild
echo %CONDA_PREFIX%
python -m pytest --verbose --junit-xml reports/unit_tests.xml
