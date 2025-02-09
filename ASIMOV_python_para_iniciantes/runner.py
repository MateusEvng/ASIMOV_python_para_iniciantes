import sys
from streamlit.web import cli as stcli

#localhost:8501

sys.argv = ["streamlit", "run", "app.py"]
sys.exit(stcli.main())