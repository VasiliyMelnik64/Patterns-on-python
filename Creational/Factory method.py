from abc import abstractmethod


class Service:
    def create_api():
        pass


class ServiceCreator:
    @abstractmethod
    def create_service() -> Service:
        pass


class AuthServiceCreator(ServiceCreator):
    def create_service(self) -> Service:
        return AuthService()


class FetchDataServiceCreator(ServiceCreator):
    def create_service(self) -> Service:
        return FetchDataService()


class AuthService(Service):
    def create_api(self) -> None:
        print('Auth API created')


class FetchDataService(Service):
    def create_api(self) -> None:
        print('FetchData API created')


AuthService().create_api()
FetchDataService().create_api()
