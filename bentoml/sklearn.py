# ==============================================================================
#     Copyright (c) 2021 Atalaya Tech. Inc
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
# ==============================================================================

import typing as t

from ._internal.artifacts import ModelArtifact
from ._internal.exceptions import MissingDependencyException
from ._internal.types import MetadataType, PathType


class SklearnModel(ModelArtifact):
    """
    Model class for saving/loading :obj:`sklearn` models.

    Args:
        model (`Any`, that is omitted by `sklearn`):
            Any model that is omitted by `sklearn`
        metadata (`Dict[str, Any]`,  `optional`, default to `None`):
            Class metadata

    Raises:
        MissingDependencyException:
            :obj:`sklearn` is required by SklearnModel

    Example usage under :code:`train.py`::

        TODO:

    One then can define :code:`bento_service.py`::

        TODO:

    Pack bundle under :code:`bento_packer.py`::

        TODO:
    """

    try:
        import joblib
    except ImportError:
        try:
            from sklearn.externals import joblib
        except ImportError:
            raise MissingDependencyException(
                "sklearn module is required to use SklearnModel"
            )

    def __init__(self, model, metadata: t.Optional[MetadataType] = None):
        super(SklearnModel, self).__init__(model, metadata=metadata)

    @classmethod
    def __get_file__path(cls, path: PathType) -> PathType:
        return cls.get_path(path, cls.PICKLE_EXTENSION)

    @classmethod
    def load(cls, path: PathType) -> t.Any:
        try:
            import joblib
        except ImportError:
            try:
                from sklearn.externals import joblib
            except ImportError:
                raise MissingDependencyException(
                    "sklearn module is required to use SklearnModel"
                )
        return joblib.load(cls.__get_file__path(path), mmap_mode="r")

    def save(self, path: PathType) -> None:
        try:
            import joblib
        except ImportError:
            try:
                from sklearn.externals import joblib
            except ImportError:
                raise MissingDependencyException(
                    "sklearn module is required to use SklearnModel"
                )
        joblib.dump(self._model, self.__get_file__path(path))