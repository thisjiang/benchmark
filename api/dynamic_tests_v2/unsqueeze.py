#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
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

from common_import import *
import numpy as np


class UnsqueezeConfig(APIConfig):
    def __init__(self):
        super(UnsqueezeConfig, self).__init__("unsqueeze")

    def init_from_json(self, filename, config_id=0, unknown_dim=16):
        super(UnsqueezeConfig, self).init_from_json(filename, config_id,
                                                    unknown_dim)
        if self.axis == [2]:
            self.axis = 2


class PDUnsqueeze(PaddleDynamicAPIBenchmarkBase):
    def build_graph(self, config):
        x = self.variable(name="x", shape=config.x_shape, dtype=config.x_dtype)
        result = paddle.unsqueeze(x=x, axis=config.axis)

        self.feed_list = [x]
        self.fetch_list = [result]
        if config.backward:
            self.append_gradients(result, [x])


class TorchUnsqueeze(PytorchAPIBenchmarkBase):
    def build_graph(self, config):
        x = self.variable(name='x', shape=config.x_shape, dtype=config.x_dtype)
        result = torch.unsqueeze(input=x, dim=config.axis)

        self.feed_list = [x]
        self.fetch_list = [result]
        if config.backward:
            self.append_gradients(result, [x])


if __name__ == '__main__':
    test_main(
        pd_dy_obj=PDUnsqueeze(),
        torch_obj=TorchUnsqueeze(),
        config=UnsqueezeConfig())
