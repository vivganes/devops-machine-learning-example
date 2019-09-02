conda init bash
activate mybuild && echo "hello" $CONDA_PREFIX &&v python -m pytest --verbose --junit-xml reports/unit_tests.xml
