from abc import abstractmethod


class IService:
    def create_api():
        pass


class ServiceCreator:
    @abstractmethod
    def create_service() -> IService:
        # might me their own logic
        pass


class AuthServiceCreator(ServiceCreator):
    def create_service(self) -> IService:
        # might me their own logic
        return AuthService()


class FetchDataServiceCreator(ServiceCreator):
    def create_service(self) -> IService:
        # might me their own logic
        return FetchDataService()


class AuthService(IService):
    def create_api(self) -> None:
        # the rest logic
        print('Auth API created')


class FetchDataService(IService):
    def create_api(self) -> None:
        # the rest logic
        print('FetchData API created')


AuthService().create_api()
FetchDataService().create_api()
