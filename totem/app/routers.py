from blacksheep import RoutesRegistry, Router

api_router = Router()
api_controllers_router = RoutesRegistry()

get = api_controllers_router.get
post = api_controllers_router.post
delete = api_controllers_router.delete
patch = api_controllers_router.patch
