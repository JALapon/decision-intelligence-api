# Simple in-memory job store
class JobStore:
    # Initialize the job store
    def __init__(self):
        self.jobs = {}

    # Create a new job entry
    def create(self, job_id):
        self.jobs[job_id] = {"status": "queued"}

    # Update job status and result
    def update(self, job_id, status, result=None):
        self.jobs[job_id]["status"] = status
        self.jobs[job_id]["result"] = result

    # Retrieve job information
    def get(self, job_id):
        return self.jobs.get(job_id)

# Instantiate a global job store
job_store = JobStore()
