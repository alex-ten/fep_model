def f(*args, **kwargs):
    pass


def k_delta(x1, x2):
    '''_summary_

    Parameters
    ----------
    x1 : float
    x2 : float

    Returns
    -------
    float 0.0 or 1.0
        If x1 and x2 are equal return 1.0, otherwise return 0.0
    '''
    if x1 == x2:
        return 1.0
    else:
        return 0.0


def transition_probability(new_state, old_state, action, theta):
    '''_summary_

    Parameters
    ----------
    new_state : _type_
        _description_
    old_state : _type_
        _description_
    action : _type_
        _description_
    theta : _type_
        subjective transition parameter

    Returns
    -------
    _type_
        Subjective probability of transitioning from old state to new state, given action and belief
    '''
    proba = f(new_state, old_state, action, theta)  # <- some function of old_state, action, and theta
    return proba


# ENVIRONMENT
# ===

# Hard-code state and action spaces
states, actions = list(), list()

# Hard-code transitions in the environment
transitions = object    # <- unknown to the agent

# Hard-code transition probabilities in a theta object (dictionary)
real_transition_proba = {}
for new_state in states:
    for action in actions:
        for old_state in states:
            real_transition_proba[new_state] = k_delta(new_state, transitions(old_state, action))


# AGENT KNOWLEDGE
# ===

def q(theta, alpha):
    return dirichlet(theta, alpha)