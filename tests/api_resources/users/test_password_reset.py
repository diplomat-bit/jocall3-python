# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from garbage import Garbage, AsyncGarbage
from tests.utils import assert_matches_type
from garbage.types.users import (
    PasswordResetConfirmResponse,
    PasswordResetInitiateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPasswordReset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_confirm(self, client: Garbage) -> None:
        password_reset = client.users.password_reset.confirm(
            identifier="string",
            new_password="string",
            verification_code="string",
        )
        assert_matches_type(PasswordResetConfirmResponse, password_reset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_confirm(self, client: Garbage) -> None:
        response = client.users.password_reset.with_raw_response.confirm(
            identifier="string",
            new_password="string",
            verification_code="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password_reset = response.parse()
        assert_matches_type(PasswordResetConfirmResponse, password_reset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_confirm(self, client: Garbage) -> None:
        with client.users.password_reset.with_streaming_response.confirm(
            identifier="string",
            new_password="string",
            verification_code="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password_reset = response.parse()
            assert_matches_type(PasswordResetConfirmResponse, password_reset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate(self, client: Garbage) -> None:
        password_reset = client.users.password_reset.initiate(
            identifier="string",
        )
        assert_matches_type(PasswordResetInitiateResponse, password_reset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate(self, client: Garbage) -> None:
        response = client.users.password_reset.with_raw_response.initiate(
            identifier="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password_reset = response.parse()
        assert_matches_type(PasswordResetInitiateResponse, password_reset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate(self, client: Garbage) -> None:
        with client.users.password_reset.with_streaming_response.initiate(
            identifier="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password_reset = response.parse()
            assert_matches_type(PasswordResetInitiateResponse, password_reset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPasswordReset:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_confirm(self, async_client: AsyncGarbage) -> None:
        password_reset = await async_client.users.password_reset.confirm(
            identifier="string",
            new_password="string",
            verification_code="string",
        )
        assert_matches_type(PasswordResetConfirmResponse, password_reset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncGarbage) -> None:
        response = await async_client.users.password_reset.with_raw_response.confirm(
            identifier="string",
            new_password="string",
            verification_code="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password_reset = await response.parse()
        assert_matches_type(PasswordResetConfirmResponse, password_reset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncGarbage) -> None:
        async with async_client.users.password_reset.with_streaming_response.confirm(
            identifier="string",
            new_password="string",
            verification_code="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password_reset = await response.parse()
            assert_matches_type(PasswordResetConfirmResponse, password_reset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate(self, async_client: AsyncGarbage) -> None:
        password_reset = await async_client.users.password_reset.initiate(
            identifier="string",
        )
        assert_matches_type(PasswordResetInitiateResponse, password_reset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate(self, async_client: AsyncGarbage) -> None:
        response = await async_client.users.password_reset.with_raw_response.initiate(
            identifier="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password_reset = await response.parse()
        assert_matches_type(PasswordResetInitiateResponse, password_reset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate(self, async_client: AsyncGarbage) -> None:
        async with async_client.users.password_reset.with_streaming_response.initiate(
            identifier="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password_reset = await response.parse()
            assert_matches_type(PasswordResetInitiateResponse, password_reset, path=["response"])

        assert cast(Any, response.is_closed) is True
