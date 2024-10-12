# coding: utf-8

"""
    mpijob

    Python SDK for MPI-Operator  # noqa: E501

    The version of the OpenAPI document: v2beta1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mpijob
from mpijob.models.k8s_io_apimachinery_pkg_version_info import K8sIoApimachineryPkgVersionInfo  # noqa: E501
from mpijob.rest import ApiException

class TestK8sIoApimachineryPkgVersionInfo(unittest.TestCase):
    """K8sIoApimachineryPkgVersionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test K8sIoApimachineryPkgVersionInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mpijob.models.k8s_io_apimachinery_pkg_version_info.K8sIoApimachineryPkgVersionInfo()  # noqa: E501
        if include_optional :
            return K8sIoApimachineryPkgVersionInfo(
                build_date = '', 
                compiler = '', 
                git_commit = '', 
                git_tree_state = '', 
                git_version = '', 
                go_version = '', 
                major = '', 
                minor = '', 
                platform = ''
            )
        else :
            return K8sIoApimachineryPkgVersionInfo(
                build_date = '',
                compiler = '',
                git_commit = '',
                git_tree_state = '',
                git_version = '',
                go_version = '',
                major = '',
                minor = '',
                platform = '',
        )

    def testK8sIoApimachineryPkgVersionInfo(self):
        """Test K8sIoApimachineryPkgVersionInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()