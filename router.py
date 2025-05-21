from typing import Annotated
from fastapi import APIRouter, Depends
from schemas import TaskAddSchema, TaskSchema
from repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get(path="", summary="get all tasks")
async def get_tasks() -> list[TaskSchema]:
    tasks = await TaskRepository.get_all()
    return tasks

@router.post(path="", summary="add one task")
async def add_task(task: Annotated[TaskAddSchema, Depends()]) -> TaskSchema:
    task = await TaskRepository.add_one(task)
    return task