from abc import abstractmethod, ABC

import numpy as np
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_is_fitted

from ..utils import construct_pandas_obj, plot_anomaly_score, plot_roc_curve


class BaseDetector(BaseEstimator, ABC):
    """Base class for all detectors."""

    _estimator_type    = 'detector'

    plot_anomaly_score = plot_anomaly_score
    plot_roc_curve     = plot_roc_curve

    @abstractmethod
    def check_params(self):
        """Check validity of parameters and raise ValueError if not valid."""

    @abstractmethod
    def fit(self, X, y=None, **fit_params):
        """Fit the model according to the given training data."""

    @abstractmethod
    def anomaly_score(self, X=None):
        """Compute anomaly scores for test samples."""

    @construct_pandas_obj
    def detect(self, X=None, threshold=None):
        """Detect if a particular sample is an outlier or not.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features), default None
            Test samples.

        threshold : float, default None
            User-provided threshold.

        Returns
        -------
        y_pred : array-like of shape (n_samples,)
            Return 1 for inliers and -1 for outliers.
        """

        check_is_fitted(self, 'threshold_')

        if threshold is None:
            threshold = self.threshold_

        return np.where(self.anomaly_score(X) <= threshold, 1, -1)

    def fit_detect(self, X, y=None, threshold=None, **fit_params):
        """Fit the model according to the given training data and detect if a
        particular sample is an outlier or not.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Samples.

        threshold : float, default None
            User-provided threshold.

        Returns
        -------
        y_pred : array-like of shape (n_samples,)
            Return 1 for inliers and -1 for outliers.
        """

        return self.fit(X, **fit_params).detect(threshold=threshold)

    def score(X, y, threshold=None):
        """Return the F1 score on the given test data and labels.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Test samples.

        y : array-like of shape (n_samples,)
            True labels for test samples.

        Returns
        -------
        score : float
            F1 score.
        """

        return f1_score(y, self.detect(X, threshold=threshold))


class AnalyzerMixin:
    """Mixin class for all analyzers."""

    @abstractmethod
    def feature_wise_anomaly_score(self, X=None):
        """Compute feature-wise anomaly scores for test samples."""

    @construct_pandas_obj
    def analyze(self, X=None, y=None, feature_wise_threshold=None):
        """Analyze which features contribute to anomalies.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features), default None
            Samples.

        feature_wise_threshold : ndarray of shape (n_features,), default None
            User-provided feature-wise threshold.

        Returns
        -------
        Y_pred : array-like of shape (n_samples, n_features)
        """

        check_is_fitted(self, 'feature_wise_threshold_')

        if feature_wise_threshold is None:
            feature_wise_threshold = self.feature_wise_threshold_

        return np.where(
            self.feature_wise_anomaly_score(X) > feature_wise_threshold, -1, 1
        )

    def fit_analyze(self, X, y=None, **fit_params):
        """Fit the model according to the given training data and analyze which
        features contribute to anomalies.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Samples.

        Returns
        -------
        Y_pred : array-like of shape (n_samples, n_features)
        """

        return self.fit(X, **fit_params).analyze()
