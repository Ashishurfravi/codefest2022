# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext, StatePropertyAccessor
from botbuilder.schema import ChannelAccount, CardAction, ActionTypes, SuggestedActions
from botbuilder.dialogs import Dialog


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    # async def on_message_activity(self, turn_context: TurnContext):
        # await turn_context.send_activity(f"{ turn_context.activity.text }!")
        # return await self._send_suggested_actions(turn_context)
        
    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Welcome to Start Young UK !")
                await turn_context.send_activity("May I know your name?")

    async def _send_suggested_actions(self, turn_context: TurnContext):
        reply = MessageFactory.text("There are various ways to help and support us. Please select one of the below given options.")
        reply.suggested_actions = SuggestedActions(
            actions=[
                CardAction(
                    title="Sponsor A Child",
                    type=ActionTypes.im_back,
                    value="Sponsor A Child",
                ),
                CardAction(
                    title="Become a Campaigner (Spread the word)",
                    type=ActionTypes.im_back,
                    value="Become a Campaigner (Spread the word)",
                ),
                CardAction(
                    title="Donate",
                    type=ActionTypes.im_back,
                    value="Donate",
                ),
                CardAction(
                    title="Become a Mentor",
                    type=ActionTypes.im_back,
                    value="Become a Mentor",
                ),
            ]
        )
        await turn_context.send_activity(reply)
