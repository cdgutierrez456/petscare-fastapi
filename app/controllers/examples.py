from sqlalchemy import update, delete, func, and_, or_

# Obtiene todos los usuarios activos que sean admin o manager
async def getUsersAdminOrManage():
    query = select(User).where(
        and_(
            User.is_active == True,
            or_(User.role == "admin", User.role == "manager")
        )
    )
    result = await db.execute(query)
    users = result.scalars().all()
    # scalars


# users → [(1, 'user@mail.com'), (2, 'admin@mail.com'), ...]
async def getSomeColumns():
    query = select(User.id, User.email).where(User.is_active == True)
    result = await db.execute(query)
    users = result.all()

# Desactiva un usuario específico sin tener que hacer .get() primero
async def updateUser():
    query = (
        update(User)
        .where(User.email == "test@mail.com")
        .values(is_active=False)
        .execution_options(synchronize_session="fetch")
    )
    await db.execute(query)
    await db.commit()

# Obtiene todos los usuarios cuyo perfil se llame “Admin”.
async def getAllAdminUsers():
    query = (
        select(User, Profile)
        .join(Profile, User.profile_id == Profile.id_profile)
        .where(Profile.name == "Admin")
    )
    result = await db.execute(query)
    users = result.scalars().all()
    return users

# Devuelve el número total de usuarios activos
async def getTotalUsers():
    query = select(func.count(User.id)).where(User.is_active == True)
    result = await db.execute(query)
    total_users = result.scalar_one()
    return total_users