from sqlalchemy import select
from database import new_session, TaskORM
from schemas import TaskAddSchema, TaskSchema

class TaskRepository:

    @classmethod
    async def get_all(cls) -> list[TaskSchema]:
        async with new_session() as session:
            query = select(TaskORM) # Выбор таблицы
            result = await session.execute(query) # execute - выполнение инструкций
            tasks = result.scalars().all()
            task_schemas = [TaskSchema.model_validate(task) for task in tasks] # приведение к аннотации типов
            return task_schemas

    @classmethod
    async def get_one(cls):
        ...

    @classmethod
    async def get_limit(cls):
        ...

    @classmethod
    async def add_one(cls, data: TaskAddSchema) -> TaskSchema:
        async with new_session() as session:
            task_dict = data.model_dump() # преобразование в словарь
            task = TaskORM(**task_dict) # из словаря в заполненную схему
            session.add(task)
            await session.flush() # получение id
            await session.commit() # принятие изменений
            return task

    @classmethod
    async def add_several(cls):
        ...

    @classmethod
    async def delete_one(cls):
        ...

    @classmethod
    async def delete_several(cls):
        ...

    @classmethod
    async def delete_limit(cls):
        ...