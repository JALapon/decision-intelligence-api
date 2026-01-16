class JobStore:
    def __init__(self):
        self.jobs = {}

    def create(self, job_id):
        self.jobs[job_id] = {"status": "queued"}

    def update(self, job_id, status, result=None):
        self.jobs[job_id]["status"] = status
        self.jobs[job_id]["result"] = result

    def get(self, job_id):
        return self.jobs.get(job_id)

job_store = JobStore()
