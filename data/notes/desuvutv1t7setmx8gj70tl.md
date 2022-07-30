
- Areas: [[devlog.linux]]

---

`fg` command moves a [[background process|background job]] in the current shell environment into the [[foreground process|foreground]]. Use the job ID parameter to indicate a specific job to be run in the foreground. If this parameter is not supplied, the `fg` command uses the job most recently suspended, placed in the background, or run as a background job.

`fg %JobID`
