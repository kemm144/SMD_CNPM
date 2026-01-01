from infrastructure.databases.mssql import init_mssql
from infrastructure.models import todo_model, user_model, faculties_model, academicYears_model, assessmentSchemes_model, syllabusComments_model, syllabuses_model, workflowLogs_model 

def init_db(app):
    init_mssql(app)
    
from infrastructure.databases.mssql import Base