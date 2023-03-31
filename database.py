from sqlalchemy import create_engine,text

db_connection_string= "mysql+pymysql://l9dyp41ijpctbpybkq4w:pscale_pw_G3bX2msbFNIQeAcj73XiJYmaD0ierOlG8fs2OOgpq5y@aws.connect.psdb.cloud/automationcarrer?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
  "ssl": {
  "ssl_ca": "/etc/ssl/cert.pem"         
      }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row)
    return jobs
