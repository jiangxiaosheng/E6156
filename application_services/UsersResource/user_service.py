from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service


class UserResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_all_users(cls):
        res = d_service.find_by_template('E6156', 'users',
                                         None, None)
        return res

    @classmethod
    def get_by_user_no(cls, user_no):
        res = d_service.find_by_template("E6156", "users",
                                         {'user_no': user_no}, None)
        return res