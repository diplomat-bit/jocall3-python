# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from garbage import Garbage, AsyncGarbage
from tests.utils import assert_matches_type
from garbage.types.ai.oracle import (
    PredictionRetrieveInflationResponse,
    PredictionRetrieveMarketCrashProbabilityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPredictions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_inflation(self, client: Garbage) -> None:
        prediction = client.ai.oracle.predictions.retrieve_inflation()
        assert_matches_type(PredictionRetrieveInflationResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_inflation_with_all_params(self, client: Garbage) -> None:
        prediction = client.ai.oracle.predictions.retrieve_inflation(
            region="region",
        )
        assert_matches_type(PredictionRetrieveInflationResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_inflation(self, client: Garbage) -> None:
        response = client.ai.oracle.predictions.with_raw_response.retrieve_inflation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionRetrieveInflationResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_inflation(self, client: Garbage) -> None:
        with client.ai.oracle.predictions.with_streaming_response.retrieve_inflation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionRetrieveInflationResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_market_crash_probability(self, client: Garbage) -> None:
        prediction = client.ai.oracle.predictions.retrieve_market_crash_probability()
        assert_matches_type(PredictionRetrieveMarketCrashProbabilityResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_market_crash_probability(self, client: Garbage) -> None:
        response = client.ai.oracle.predictions.with_raw_response.retrieve_market_crash_probability()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionRetrieveMarketCrashProbabilityResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_market_crash_probability(self, client: Garbage) -> None:
        with client.ai.oracle.predictions.with_streaming_response.retrieve_market_crash_probability() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionRetrieveMarketCrashProbabilityResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPredictions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_inflation(self, async_client: AsyncGarbage) -> None:
        prediction = await async_client.ai.oracle.predictions.retrieve_inflation()
        assert_matches_type(PredictionRetrieveInflationResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_inflation_with_all_params(self, async_client: AsyncGarbage) -> None:
        prediction = await async_client.ai.oracle.predictions.retrieve_inflation(
            region="region",
        )
        assert_matches_type(PredictionRetrieveInflationResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_inflation(self, async_client: AsyncGarbage) -> None:
        response = await async_client.ai.oracle.predictions.with_raw_response.retrieve_inflation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionRetrieveInflationResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_inflation(self, async_client: AsyncGarbage) -> None:
        async with async_client.ai.oracle.predictions.with_streaming_response.retrieve_inflation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionRetrieveInflationResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_market_crash_probability(self, async_client: AsyncGarbage) -> None:
        prediction = await async_client.ai.oracle.predictions.retrieve_market_crash_probability()
        assert_matches_type(PredictionRetrieveMarketCrashProbabilityResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_market_crash_probability(self, async_client: AsyncGarbage) -> None:
        response = await async_client.ai.oracle.predictions.with_raw_response.retrieve_market_crash_probability()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionRetrieveMarketCrashProbabilityResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_market_crash_probability(self, async_client: AsyncGarbage) -> None:
        async with (
            async_client.ai.oracle.predictions.with_streaming_response.retrieve_market_crash_probability()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionRetrieveMarketCrashProbabilityResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True
