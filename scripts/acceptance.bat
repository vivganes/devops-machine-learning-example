CALL conda.bat activate mybuild
echo %CONDA_PREFIX%
behave -f=formatters.cucumber_json:PrettyCucumberJSONFormatter -o ./reports/acceptance.json
