#!/usr/bin/env python
# Copyright (C) 2015 Swift Navigation Inc.
# Contact: Ian Horn <ian@swiftnav.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.


from gnss_analysis.abstract_analysis.analysis import *
from gnss_analysis.abstract_analysis.report import *
import gnss_analysis.utils as ut
import swiftnav.dgnss_management as mgmt

# Inspection for the internals of the KF state.

class KFSats(Analysis):
  """
  The sats used by the KF.
  """
  def __init__(self):
    super(KFSats, self).__init__(
      key='KFSats',
      keep_as_map=True)
  def compute(self, data, current_analyses, prev_fold, parameters):
    prns = mgmt.get_sats_management()[1]
    if len(prns) < 2:
      return None
    return prns[0], prns[1:]

class KFNumSats(Analysis):
  """
  How many sats the KF is using.
  """
  def __init__(self):
    super(KFNumSats, self).__init__(
      key='KFNumSats',
      keep_as_map=True)
  def compute(self, data, current_analyses, prev_fold, parameters):
    prns = mgmt.get_sats_management()[1]
    if len(prns) < 2:
      return 0
    return len(prns)

class KFMean(Analysis):
  """
  The KF state estimates.
  """
  def __init__(self):
    super(KFMean, self).__init__(
      key='KFMean',
      keep_as_map=True)
  def compute(self, data, current_analyses, prev_fold, parameters):
    return mgmt.get_amb_kf_mean()

class KFCov(Analysis):
  """
  The KF state estimate covariance matrix.
  """
  def __init__(self):
    super(KFCov, self).__init__(
      key='KFCov',
      keep_as_map=True)
  def compute(self, data, current_analyses, prev_fold, parameters):
    return mgmt.get_amb_kf_cov2()

class KFSatsR(Report):
  """
  A time series of sats used by the KF.
  """
  def __init__(self):
    super(KFSatsR, self).__init__(
      key="KFSats",
      parents=set([KFSats()]))
  def report(self, data, analyses, folds, parameters):
    return analyses['KFSats']

class KFNumSatsR(Report):
  """
  A time series of how many sats are used by the KF.
  """
  def __init__(self):
    super(KFNumSatsR, self).__init__(
      key="KFNumSats",
      parents=set([KFNumSats()]))
  def report(self, data, analyses, folds, parameters):
    return analyses['KFNumSats']

class KFMeanR(Report):
  """
  A time series of KF state estimates.
  """
  def __init__(self):
    super(KFMeanR, self).__init__(
      key="KFMean",
      parents=set([KFMean()]))
  def report(self, data, analyses, folds, parameters):
    return analyses['KFMean']

class KFCovR(Report):
  """
  A time series of KF state estimate covariance matrices.
  """
  def __init__(self):
    super(KFCovR, self).__init__(
      key="KFCov",
      parents=set([KFCov()]))
  def report(self, data, analyses, folds, parameters):
    return analyses['KFCov']
