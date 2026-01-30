# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from garbage import Garbage, AsyncGarbage
from tests.utils import assert_matches_type
from garbage.types import MarketplaceListProductsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarketplace:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_products(self, client: Garbage) -> None:
        marketplace = client.marketplace.list_products()
        assert_matches_type(MarketplaceListProductsResponse, marketplace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_products(self, client: Garbage) -> None:
        response = client.marketplace.with_raw_response.list_products()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketplace = response.parse()
        assert_matches_type(MarketplaceListProductsResponse, marketplace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_products(self, client: Garbage) -> None:
        with client.marketplace.with_streaming_response.list_products() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketplace = response.parse()
            assert_matches_type(MarketplaceListProductsResponse, marketplace, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarketplace:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_products(self, async_client: AsyncGarbage) -> None:
        marketplace = await async_client.marketplace.list_products()
        assert_matches_type(MarketplaceListProductsResponse, marketplace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_products(self, async_client: AsyncGarbage) -> None:
        response = await async_client.marketplace.with_raw_response.list_products()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketplace = await response.parse()
        assert_matches_type(MarketplaceListProductsResponse, marketplace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_products(self, async_client: AsyncGarbage) -> None:
        async with async_client.marketplace.with_streaming_response.list_products() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketplace = await response.parse()
            assert_matches_type(MarketplaceListProductsResponse, marketplace, path=["response"])

        assert cast(Any, response.is_closed) is True
