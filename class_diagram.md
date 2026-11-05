# Class Diagram — Current Sprint: Sprint 4

> **Living document.** Updated when architecture changes. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S4_1

---

```mermaid
classDiagram
    class Task {
        +int id
        +str title
        +str description
        +bool completed
        +mark_complete() None
        +to_dict() dict
    }

    class ITaskRepository {
        <<abstract>>
        +add_task(title, description)*
        +get_all_tasks()*
        +complete_task(task_id)*
        +delete_task(task_id)*
        +clear_tasks()*
    }

    class FileTaskRepository {
        +add_task(title, description) dict
        +get_all_tasks() list
        +complete_task(task_id) dict | None
        +delete_task(task_id) dict | None
        +clear_tasks() None
    }

    class DatabaseTaskRepository {
        +add_task(title, description) dict
        +get_all_tasks() list
        +complete_task(task_id) dict | None
        +delete_task(task_id) dict | None
        +clear_tasks() None
    }

    class TaskStorage {
        +load_tasks() list
        +save_tasks(tasks) None
    }

    class TaskService {
        +__init__(repository: ITaskRepository)
        +add_task(title, description) dict
        +get_all_tasks() list
        +complete_task(task_id) dict | None
        +delete_task(task_id) dict | None
        +clear_tasks() None
    }

    class FlaskApp {
        +create_app(service, use_db) Flask
        +task_service: TaskService
    }

    class TaskRoutes {
        +POST /api/tasks
        +GET /api/tasks
        +PUT /api/tasks/id
        +DELETE /api/tasks/id
        +POST /api/tasks/reset
    }

    ITaskRepository <|-- FileTaskRepository : implements
    ITaskRepository <|-- DatabaseTaskRepository : implements
    FileTaskRepository --> TaskStorage : wraps
    TaskService --> ITaskRepository : depends on interface
    TaskService --> Task : creates/manages
    FlaskApp --> TaskService : injects via create_app()
    FlaskApp --> TaskRoutes : registers blueprint
    TaskRoutes --> TaskService : current_app.task_service
```

## Key Relationships

| Relationship | From | To | Type |
|---|---|---|---|
| Interface | `ITaskRepository` | `FileTaskRepository` | Inheritance (implements ABC) |
| Interface | `ITaskRepository` | `DatabaseTaskRepository` | Inheritance (implements ABC) |
| Dependency | `TaskService` | `ITaskRepository` | Depends on interface — not concrete class |
| Wraps | `FileTaskRepository` | `TaskStorage` | Delegation |
| Injection | `FlaskApp` | `TaskService` | Dependency Injection |

## Notes

- `TaskService` now depends on `ITaskRepository` — not `TaskStorage` directly
- `MockTaskService` (hand-rolled) is **removed** — `mocker.MagicMock()` replaces it
- `DatabaseTaskRepository` shown here but implemented in S4_2
