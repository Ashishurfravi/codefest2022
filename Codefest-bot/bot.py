# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from os import system
import re
from time import sleep
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount, CardAction, ActionTypes, SuggestedActions


class MyBot(ActivityHandler):
    """
    This bot will respond to the user's input with suggested actions.
    Suggested actions enable your bot to present buttons that the user
    can tap to provide input.
    """
    async def on_members_added_activity(
        self, members_added: ChannelAccount, turn_context: TurnContext
    ):
        """
        Send a welcome message to the user and tell them what actions they may perform to use this bot
        """
        return await self._send_welcome_message(turn_context)

    async def on_message_activity(self, turn_context: TurnContext):
        """
        Respond to the users choice and display the suggested actions again.
        """
        text = turn_context.activity.text
        response_text = self._process_input(text)
        try:
            if "donate monthly" in response_text:
                await turn_context.send_activity(MessageFactory.text(response_text))
                return await self._donation_input(turn_context)
            if response_text.startswith("Hi "):
                await turn_context.send_activity(MessageFactory.text(response_text))
                return await self._send_suggested_actions(turn_context)
            await turn_context.send_activity(MessageFactory.text(response_text))
            sleep(1) 
        except TypeError as e:
            await turn_context.send_activity("Thanks for contacting us, will reach out to you.")
            sleep(1)        

    async def _send_welcome_message(self, turn_context: TurnContext):
        for member in turn_context.activity.members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    MessageFactory.text(f"Welcome to Start Young UK !")
                )
                sleep(1)
                return await turn_context.send_activity("May I know your name?")

    def _process_input(self, text1: str):
        if text1 == "Sponsor A Child":
            sleep(1)
            return f"Would you like to donate monthly or one time?"
        if text1 == "Become a Campaigner":
            sleep(1)
            return f"Please enter your email id and we will get back to you"
        if text1 == "Donate":
            sleep(1)
            return f"Would you like to donate monthly or one time?"
        if text1 == "Become a Mentor":
            sleep(1)
            return f"Please enter your email id and we will get back to you"
        sleep(1) 
        if text1 != "Monthly" and text1 != "One Time" and ".com" not in text1:
            return f"Hi {text1} !"
        if "@" in text1 or ".com" in text1:
            return f"Thanks for contacting us, will reach out to you."
        if text1 != "Monthly" or text1 != "One Time":
            sleep(1)
            return f"Please enter your email id and we will get back to you"
        

    async def _send_suggested_actions(self, turn_context: TurnContext):
        """
        Creates and sends an activity with suggested actions to the user. When the user
        clicks one of the buttons the text value from the "CardAction" will be displayed
        in the channel just as if the user entered the text. There are multiple
        "ActionTypes" that may be used for different situations.
        """
        reply = MessageFactory.text("There are various ways to help and support us. Please select one of the below given options.")
        reply.suggested_actions = SuggestedActions(
            actions=[
                CardAction(
                    title="Sponsor A Child",
                    type=ActionTypes.im_back,
                    value="Sponsor A Child",
                ),
                CardAction(
                    title="Become a Campaigner",
                    type=ActionTypes.im_back,
                    value="Become a Campaigner",
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
                )
            ]
        )
        await turn_context.send_activity(reply)

    async def _donation_input(self, turn_context: TurnContext):
        reply = MessageFactory.text(f"Select One")
        reply.suggested_actions = SuggestedActions(
            actions=[
                CardAction(
                    title="Monthly",
                    type=ActionTypes.im_back,
                    value="Monthly",
                ),
                CardAction(
                    title="One Time",
                    type=ActionTypes.im_back,
                    value="One Time",
                )
            ]
        )
        #return await turn_context.send_activity(reply)
        return await turn_context.send_activity(reply)