# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from garbage import Garbage, AsyncGarbage
from tests.utils import assert_matches_type
from garbage.types.ai import AgentRetrieveCapabilitiesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_capabilities(self, client: Garbage) -> None:
        agent = client.ai.agent.retrieve_capabilities()
        assert_matches_type(AgentRetrieveCapabilitiesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_capabilities(self, client: Garbage) -> None:
        response = client.ai.agent.with_raw_response.retrieve_capabilities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveCapabilitiesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_capabilities(self, client: Garbage) -> None:
        with client.ai.agent.with_streaming_response.retrieve_capabilities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveCapabilitiesResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_capabilities(self, async_client: AsyncGarbage) -> None:
        agent = await async_client.ai.agent.retrieve_capabilities()
        assert_matches_type(AgentRetrieveCapabilitiesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_capabilities(self, async_client: AsyncGarbage) -> None:
        response = await async_client.ai.agent.with_raw_response.retrieve_capabilities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveCapabilitiesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_capabilities(self, async_client: AsyncGarbage) -> None:
        async with async_client.ai.agent.with_streaming_response.retrieve_capabilities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveCapabilitiesResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
