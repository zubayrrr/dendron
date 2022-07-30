
State machine is a collection of states, each state will take input from the previous state and that state will send it’s output to the next state.

AWS Step Functions lets us coordinate multiple AWS Services into [[devlog.serverless]] **workflows**. We can design and run workflows that stitch together services like [[devlog.AWS Lambda]], [[devlog.AWS Fargate]], [[devlog.AWS Sagemaker]] into feature rich applications.

- Configure: Define your workflow as a series of steps such as tasks, choices, parallel execution and timeouts.
- Populate: Connect tasks to code hosted in functions, instances and on-prem servers.
- Run: We provide any needed input and run your workflow as many times as needed for up to 1 year.
- Evolve: We can swap out tasks, change the order of steps or add new steps without changing code.

## Use cases

- Processes that extend beyond 15 minutes life of a [[devlog.AWS Lambda]] function.
- One function for one task.
- Business processes(user intervention).
- Parallel execution of Lambda functions.
