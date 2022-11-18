initialize = lambda x: x
get_state = lambda x: x
predict = lambda x: x
evaluate = lambda x: x
update = lambda x: x
choose = lambda x: x
act = lambda x: x
actions = []
n_steps = 1


model, valueF = initialize()
for step in n_steps:
    state = get_state()

    # predictions = predict(state, actions, model)
    # valueF[state] = evaluate(actions, predictions) # e.g., H, EIG, CP, surprisal

    action = choose(actions, valueF)
    observed_state = act(state, action)
    update(model, state, action, observed_state)
    valueF[state] = evaluate(actions, predictions, observed_state) # e.g., DKL, IG, PE, LP (change in PE), novelty.