from view.loging_veiw import LoginView
from view.dashboard import DashboardView
import os
# ui = LoginView()
ui= DashboardView()
print("current file",__file__)
print("abs path",os.path.abspath("db/hospital.db"))