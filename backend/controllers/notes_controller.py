from fastapi import APIRouter

router = APIRouter()

'''TODO: Return all notes'''
@router.get("/notes")
async def get_all_notes():
    return 

'''TODO: Return note by id'''
@router.get("/notes/{note_id}")
async def get_note_by_id(note_id: int):
    return 

'''TODO: Create a note'''
@router.post("/notes")
async def create_note():
    return 

'''TODO: Update a note'''
@router.put("/notes/{note_id}")
async def create_note(note_id: int):
    return 

'''TODO: Delete a note'''
@router.delete("/notes/{note_id}")
async def create_note(note_id: int):
    return 