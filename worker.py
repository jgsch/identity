
"""Copyright (C) Alpine Intuition Sàrl - All Rights Reserved.

This source code is protected under international copyright law. All rights 
reserved and protected by the copyright holders.
This file is confidential and only available to authorized individuals with the
permission of the copyright holders. If you encounter this file and do not have
permission, please contact the copyright holders and delete this file.
"""

from archipel.workers.worker import Worker

__task_class_name__ = "IdentityWorker"


class IdentityWorker(Worker):  # pragma: no cover
    """Identity Worker for benchmark purpose."""

    def setup_model(self):
        pass

    def get_dump_input(self):
        return "dump_inputs"

    def encode_input(self, data):
        return data

    def decode_input(self, data):
        return data

    def encode_output(self, data):
        return data

    def forward(self, data):
        return ""
