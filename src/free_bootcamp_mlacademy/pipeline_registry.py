"""Project pipelines."""
# from __future__ import annotations

# from kedro.framework.project import find_pipelines
# from kedro.pipeline import Pipeline


# def register_pipelines() -> dict[str, Pipeline]:
#     """Register the project's pipelines.

#     Returns:
#         A mapping from pipeline names to ``Pipeline`` objects.
#     """
#     pipelines = find_pipelines(raise_errors=True)
#     pipelines["__default__"] = sum(pipelines.values())
#     return pipelines

from .pipelines.feature_eng import feat_eng_pipeline_training, feat_eng_pipeline_inference
from .pipelines.training import create_training_pipeline
from .pipelines.inference import create_inference_pipeline
from kedro.pipeline import Pipeline

def register_pipelines() -> dict[str, Pipeline]:
    feature_eng_training = feat_eng_pipeline_training()
    feature_eng_inference = feat_eng_pipeline_inference()
    training_pipeline = create_training_pipeline()
    inference_pipeline = create_inference_pipeline()
    return {
        "__default__": feature_eng_training + training_pipeline,
        "training": feature_eng_training + training_pipeline,
        "inference": feature_eng_inference + inference_pipeline,
    }


# register_pipelines()
#         ↓
# Kedro loads pipelines
#         ↓
# kedro run
#         ↓
# runs "__default__"
#         ↓
# feature_eng → training

# This file registers and composes Kedro pipelines, defining the execution flow by combining feature engineering and training pipelines into a default pipeline that runs end-to-end.