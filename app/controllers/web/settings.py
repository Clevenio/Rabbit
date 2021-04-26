# Copyright 2022 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.views import View
from django.shortcuts import render

from app.shortcuts import Logger
from app.shortcuts import get_config
from app.controllers.controller import Controller
from app.module.settings import Settings as SettingsModule
from app.module.profile import Profile as ProfileModule


class Settings(View, Controller):
    """Settings Page Controller"""

    template_name = "templates/admin/settings.html"

    def __init__(self):
        self.profile = ProfileModule()
        self.settings = SettingsModule()
        self.logger = Logger().get_logger(__name__)

    def get(self, request):
        """
        Settings Page
        """
        data = self.settings.get_settings(
            [
                "app_name",
                "app_url",
                "app_email",
                "digitalocean_status",
                "digitalocean_api_token",
            ]
        )

        user = self.profile.get_user(request.user.id)

        profile = self.profile.get_profile(request.user.id)

        return render(
            request,
            self.template_name,
            {
                "title": get_config("app_name", "Badger"),
                "description": get_config("app_description", ""),
                "base_url": get_config("app_url", ""),
                "data": data,
                "user": user,
                "profile": profile,
            },
        )
