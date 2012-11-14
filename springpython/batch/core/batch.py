# -*- coding: utf-8 -*-

# Copyright 2006-2012 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Module to implement some Spring Batch-like features.

In particular, refer to:
    http://static.springsource.org/spring-batch/reference/html/metaDataSchema.html

As much as possible, this is copy-and-paste from the Java
implementation of the SpringBatch fraemework, hence the preservation
of the Apache license. See the original code at:

    https://github.com/SpringSource/spring-batch/tree/master/spring-batch-core/src/main/java/org/springframework/batch/core
"""

import logging


# Module-level logging instance
log = logging.getLogger(__name__)


class Job(object):
    """Batch domain object representing a job.

    Job is an explicit abstraction representing the configuration of a
    job specified by a developer. It should be noted that restart
    policy is applied to the job as a whole and not to a step.
    """
    pass


class JobParameters(object):
    """Value object representing runtime parameters to a batch job.

    Because the parameters have no individual meaning outside of the
    JobParameters they are contained within, it is a value object
    rather than an entity. It is also extremely important that a
    parameters object can be reliably compared to another for
    equality, in order to determine if one JobParameters object equals
    another. Furthermore, because these parameters will need to be
    persisted, it is vital that the types added are restricted.
    """

    parameters = {}

    def __repr__(self):
        return "<{classname}(parameters={parameters})>".format( \
            classname=self.__class__.__name__,
            parameters=self.parameters,
            )


class JobInstance(object):
    """Batch domain object representing a uniquely identifiable job run.

    Its identity is given by the pair Job and JobParameters.
    JobInstance can be restarted multiple times in case of execution
    failure and its lifecycle ends with first successful execution.

    Trying to execute an existing JobIntance that has already completed
    successfully will result in error. Error will be raised also for an attempt
    to restart a failed JobInstance if the Job is not restartable.
    """

    job_parameters = JobParameters()

    job_name = None

    def __repr__(self):
        return "<{classname}(job_name={job_name},parameters={parameters})>".format( \
            classname=self.__class__.__name__,
            job_name=self.job_name,
            parameters=self.job_parameters,
            )



