"""
LLM Abstraction System
A comprehensive, configuration-driven framework for LLM interactions

© 2025-2030 All rights reserved Ashutosh Sinha
email: ajsinha@gmail.com

This system provides:
- Unified interface for multiple LLM providers
- Configuration-driven model and provider management
- Interaction history and multi-shot learning
- Robust error handling and fallback mechanisms
- Factory, Singleton, Facade, and Delegate patterns
"""

from .core import (
    LLMProvider,
    LLMFacade,
    LLMResponse,
    LLMClient,
    LLMInteractionHistory,
    LLMProviderFactory,
    LLMClientFactory
)

from .utils import (
    ConfigLoader,
    LLMSystem,
    initialize_system
)

__version__ = '1.0.0'
__author__ = 'Ashutosh Sinha'
__email__ = 'ajsinha@gmail.com'
__copyright__ = '© 2025-2030 All rights reserved Ashutosh Sinha'

__all__ = [
    # Core classes
    'LLMProvider',
    'LLMFacade',
    'LLMResponse',
    'LLMClient',
    'LLMInteractionHistory',
    'LLMProviderFactory',
    'LLMClientFactory',
    
    # Utilities
    'ConfigLoader',
    'LLMSystem',
    'initialize_system',
    
    # Metadata
    '__version__',
    '__author__',
    '__email__',
    '__copyright__',
]
