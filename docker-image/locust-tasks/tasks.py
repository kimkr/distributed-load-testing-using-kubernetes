#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
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


import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task


class MetricsTaskSet(TaskSet):
    itemId = 47967
    userId = 'lady2810'
    
    @task(10)
    def load_js_file(self):
        self.client.get('/js/myfit-latest.js')

    @task(8)
    def get_compare_list(self):
        self.client.get("/modal/v3/mysize/attrangs?itemId={0}&userId{1}".format(self.itemId, self.userId))

    @task(1)
    def load_purchase_list(self):
        self.client.get("/modal/v3/loadOrders?brand=${0}&userId=${1}".format('ATTRANGS', self.userId))
        

class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet
