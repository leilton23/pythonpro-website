import pytest

from model_mommy import mommy

from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory


@pytest.fixture
def pre_request():
    factory = RequestFactory()
    request = factory.get('/', secure=True)
    request.user = AnonymousUser()
    return request


def _get_request_with_session_setted(pre_request):
    middleware = SessionMiddleware()
    middleware.process_request(pre_request)
    pre_request.session.save()
    return pre_request


@pytest.fixture
def mocked_request(pre_request):
    return _get_request_with_session_setted(pre_request)


@pytest.fixture
def mocked_request_2(pre_request):
    return _get_request_with_session_setted(pre_request)


@pytest.fixture
def mocked_request_logged(pre_request, logged_user):
    pre_request.user = logged_user
    middleware = SessionMiddleware()
    middleware.process_request(pre_request)
    pre_request.session.save()

    return pre_request


@pytest.fixture
def user_session(logged_user):
    return mommy.make('UserSession', user=logged_user)


@pytest.fixture
def mocked_request_with_analytics(mocked_request, user_session):
    mocked_request.session['analytics'] = {
        'id': user_session.id,
        'uuid': str(user_session.uuid)
    }
    return mocked_request
