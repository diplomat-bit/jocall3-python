# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from garbage import Garbage, AsyncGarbage
from tests.utils import assert_matches_type
from garbage.types.payments import (
    InternationalGetStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInternational:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute_sepa(self, client: Garbage) -> None:
        international = client.payments.international.execute_sepa(
            amount=4090.998569865607,
            iban="string",
        )
        assert international is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_execute_sepa(self, client: Garbage) -> None:
        response = client.payments.international.with_raw_response.execute_sepa(
            amount=4090.998569865607,
            iban="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = response.parse()
        assert international is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_execute_sepa(self, client: Garbage) -> None:
        with client.payments.international.with_streaming_response.execute_sepa(
            amount=4090.998569865607,
            iban="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = response.parse()
            assert international is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute_swift(self, client: Garbage) -> None:
        international = client.payments.international.execute_swift(
            amount=981.8703637183601,
            bic="string",
            currency="string",
            iban="string",
        )
        assert international is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_execute_swift(self, client: Garbage) -> None:
        response = client.payments.international.with_raw_response.execute_swift(
            amount=981.8703637183601,
            bic="string",
            currency="string",
            iban="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = response.parse()
        assert international is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_execute_swift(self, client: Garbage) -> None:
        with client.payments.international.with_streaming_response.execute_swift(
            amount=981.8703637183601,
            bic="string",
            currency="string",
            iban="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = response.parse()
            assert international is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Garbage) -> None:
        international = client.payments.international.get_status(
            "string",
        )
        assert_matches_type(InternationalGetStatusResponse, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Garbage) -> None:
        response = client.payments.international.with_raw_response.get_status(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = response.parse()
        assert_matches_type(InternationalGetStatusResponse, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Garbage) -> None:
        with client.payments.international.with_streaming_response.get_status(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = response.parse()
            assert_matches_type(InternationalGetStatusResponse, international, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: Garbage) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            client.payments.international.with_raw_response.get_status(
                "",
            )


class TestAsyncInternational:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute_sepa(self, async_client: AsyncGarbage) -> None:
        international = await async_client.payments.international.execute_sepa(
            amount=4090.998569865607,
            iban="string",
        )
        assert international is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_execute_sepa(self, async_client: AsyncGarbage) -> None:
        response = await async_client.payments.international.with_raw_response.execute_sepa(
            amount=4090.998569865607,
            iban="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = await response.parse()
        assert international is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_execute_sepa(self, async_client: AsyncGarbage) -> None:
        async with async_client.payments.international.with_streaming_response.execute_sepa(
            amount=4090.998569865607,
            iban="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = await response.parse()
            assert international is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute_swift(self, async_client: AsyncGarbage) -> None:
        international = await async_client.payments.international.execute_swift(
            amount=981.8703637183601,
            bic="string",
            currency="string",
            iban="string",
        )
        assert international is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_execute_swift(self, async_client: AsyncGarbage) -> None:
        response = await async_client.payments.international.with_raw_response.execute_swift(
            amount=981.8703637183601,
            bic="string",
            currency="string",
            iban="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = await response.parse()
        assert international is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_execute_swift(self, async_client: AsyncGarbage) -> None:
        async with async_client.payments.international.with_streaming_response.execute_swift(
            amount=981.8703637183601,
            bic="string",
            currency="string",
            iban="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = await response.parse()
            assert international is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncGarbage) -> None:
        international = await async_client.payments.international.get_status(
            "string",
        )
        assert_matches_type(InternationalGetStatusResponse, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncGarbage) -> None:
        response = await async_client.payments.international.with_raw_response.get_status(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = await response.parse()
        assert_matches_type(InternationalGetStatusResponse, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncGarbage) -> None:
        async with async_client.payments.international.with_streaming_response.get_status(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = await response.parse()
            assert_matches_type(InternationalGetStatusResponse, international, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncGarbage) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            await async_client.payments.international.with_raw_response.get_status(
                "",
            )
