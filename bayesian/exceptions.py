class InvalidGraphException(Exception):
    '''
    Raised if the graph verification
    method fails.
    '''
    pass


class InvalidSampleException(Exception):
    '''Should be raised if a
    sample is invalid.'''
    pass


class InvalidInferenceMethod(Exception):
    '''Raise if the user tries to set
    the inference method to an unknown string.'''
    pass


class InsufficientSamplesException(Exception):
    '''Raised when the inference method
    is 'sample_db' and there are less
    pre-generated samples than the
    graphs n_samples attribute.'''
    pass


class NoSamplesInDB(Warning):
    pass
