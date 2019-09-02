CALL conda.bat activate mybuild
echo %CONDA_PREFIX%
python setup.py bdist_wheel
