CALL conda.bat activate mybuild
echo %CONDA_PREFIX%
behave -f=json.pretty -o ./reports/integration.json
python -m behave2cucumber -i ./reports/integration.json
