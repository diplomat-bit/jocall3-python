# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from garbage import Garbage, AsyncGarbage
from tests.utils import assert_matches_type
from garbage.types.ai.incubator import (
    PitchCreateResponse,
    PitchRetrieveDetailsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPitch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Garbage) -> None:
        pitch = client.ai.incubator.pitch.create(
            business_plan="string",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="string",
        )
        assert_matches_type(PitchCreateResponse, pitch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Garbage) -> None:
        response = client.ai.incubator.pitch.with_raw_response.create(
            business_plan="string",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = response.parse()
        assert_matches_type(PitchCreateResponse, pitch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Garbage) -> None:
        with client.ai.incubator.pitch.with_streaming_response.create(
            business_plan="string",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = response.parse()
            assert_matches_type(PitchCreateResponse, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_details(self, client: Garbage) -> None:
        pitch = client.ai.incubator.pitch.retrieve_details(
            "string",
        )
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_details(self, client: Garbage) -> None:
        response = client.ai.incubator.pitch.with_raw_response.retrieve_details(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = response.parse()
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_details(self, client: Garbage) -> None:
        with client.ai.incubator.pitch.with_streaming_response.retrieve_details(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = response.parse()
            assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_details(self, client: Garbage) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pitch_id` but received ''"):
            client.ai.incubator.pitch.with_raw_response.retrieve_details(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_feedback(self, client: Garbage) -> None:
        pitch = client.ai.incubator.pitch.update_feedback(
            pitch_id="string",
            answers=[{}],
        )
        assert pitch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_feedback(self, client: Garbage) -> None:
        response = client.ai.incubator.pitch.with_raw_response.update_feedback(
            pitch_id="string",
            answers=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = response.parse()
        assert pitch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_feedback(self, client: Garbage) -> None:
        with client.ai.incubator.pitch.with_streaming_response.update_feedback(
            pitch_id="string",
            answers=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = response.parse()
            assert pitch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_feedback(self, client: Garbage) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pitch_id` but received ''"):
            client.ai.incubator.pitch.with_raw_response.update_feedback(
                pitch_id="",
                answers=[{}],
            )


class TestAsyncPitch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGarbage) -> None:
        pitch = await async_client.ai.incubator.pitch.create(
            business_plan="string",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="string",
        )
        assert_matches_type(PitchCreateResponse, pitch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGarbage) -> None:
        response = await async_client.ai.incubator.pitch.with_raw_response.create(
            business_plan="string",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = await response.parse()
        assert_matches_type(PitchCreateResponse, pitch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGarbage) -> None:
        async with async_client.ai.incubator.pitch.with_streaming_response.create(
            business_plan="string",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = await response.parse()
            assert_matches_type(PitchCreateResponse, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_details(self, async_client: AsyncGarbage) -> None:
        pitch = await async_client.ai.incubator.pitch.retrieve_details(
            "string",
        )
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_details(self, async_client: AsyncGarbage) -> None:
        response = await async_client.ai.incubator.pitch.with_raw_response.retrieve_details(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = await response.parse()
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_details(self, async_client: AsyncGarbage) -> None:
        async with async_client.ai.incubator.pitch.with_streaming_response.retrieve_details(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = await response.parse()
            assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_details(self, async_client: AsyncGarbage) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pitch_id` but received ''"):
            await async_client.ai.incubator.pitch.with_raw_response.retrieve_details(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_feedback(self, async_client: AsyncGarbage) -> None:
        pitch = await async_client.ai.incubator.pitch.update_feedback(
            pitch_id="string",
            answers=[{}],
        )
        assert pitch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_feedback(self, async_client: AsyncGarbage) -> None:
        response = await async_client.ai.incubator.pitch.with_raw_response.update_feedback(
            pitch_id="string",
            answers=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = await response.parse()
        assert pitch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_feedback(self, async_client: AsyncGarbage) -> None:
        async with async_client.ai.incubator.pitch.with_streaming_response.update_feedback(
            pitch_id="string",
            answers=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = await response.parse()
            assert pitch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_feedback(self, async_client: AsyncGarbage) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pitch_id` but received ''"):
            await async_client.ai.incubator.pitch.with_raw_response.update_feedback(
                pitch_id="",
                answers=[{}],
            )
