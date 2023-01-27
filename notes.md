# Sequential Bayesian Updating

## Introduction
The learner observed data sequentially in a series of observations and updates its knowledge with each observation:
$$O_1, ..., O_n, ...$$
where $O_i$ represents the $i$-th observation. In the monster task, observations include both the visual features of the monster stimuli and their food preferences. This is obvious, once you think of food preference as just another feature of a given monster.

Observations are used to update the inference on a latent parameter vector $\boldsymbol{\beta}$. This parameter vector represents the learner's *beliefs* about the world. In the monster task, we ask participants to learn the food preference of different monsters. In other words, their job is to estimate the latent parameters that generate the observations. Thus, participants need to learn the generative model of the data. These parameters are instantiated by us, the experimenters. That is, we have indeed set up the data-generation process so that visual features of the monsters predict their food preferences.

A generative model allows learners to make belief-based predictions. For instance, if one is convinced that big-eyed monsters like eggs, one will predict that a big-eyed monster will prefer eggs. The generative model also allows one to assess the quality of one's beliefs in light of the data. This is given by the likelihood function:

$$f(O_1,...,O_n \mid \boldsymbol\beta) = f(O_1 \mid \boldsymbol\beta) f(O_2 \mid \boldsymbol\beta) ...  f(O_n \mid \boldsymbol\beta)$$

If this likelihood is low, this should signal the learner that the beliefs do not predict the data very well. 

Prior to receiving new data, learners maintain a set of beliefs in which they can be more or less certain. Naively, we could formalize this as $\pi_0(\boldsymbol\beta)$. This could raise some eyebrows because we don't know what set of beliefs the learners may actually entertain and how they generate such sets. However, let's suppose for now that informing participants about possible links between food preferences and appearance constrains the set of hypotheses to be about visual features. And let's further assume that participants understand very quickly which visual features *might* predict food preferences by noticing their variability from one individual to the next.

At time $n=1$, the learner updates his beliefs:

$$\pi_1(\boldsymbol\beta) \propto \pi_0(\boldsymbol\beta)f(O_1 \mid \boldsymbol\beta)$$

And more generally, for $n = t$:

$$\pi_t(\boldsymbol\beta) \propto \pi_{t-1}(\boldsymbol\beta)f(O_t \mid \boldsymbol\beta)$$

## Likelihood
How do we define $f(O \mid \boldsymbol\beta)$? That is, how does the learner evaluate the likelihood of a particular observation given his beliefs? 

Suppose that $O = \{X_1, X_2, Y\}$, where $X_1$ and $X_2$ are variables denoting visual features of a monster and $Y$ denoting whether the monster likes one of the two food items. Then we could write:

$$f(O \mid \boldsymbol\beta) = p(Y = 1|X_1, X_2; \boldsymbol\beta) = \frac{1}{1 + \exp\big(-(\beta_0 + \beta_1X_1 + \beta_2X_2)\big)}$$

Here, $\beta_0$ represents the belief about the baseline preference for food #1. $\beta_1$ and $\beta_2$ represent the dependency between $X_1$ and food preference and between $X_2$ and food preference.

## Learning as Bayesian Updating
The Bayes theorem tells us how prior beliefs can be updated by observing new data:

$$\pi_t(\boldsymbol\beta \mid O_t) = \pi_n(\boldsymbol\beta) \frac{f(O_t \mid \boldsymbol\beta)}{f(O_t)}$$

In practice, we will rely on sampling methods for estimating this the posterior distribution (e.g., `pymc3`).

Note that the Bayes rule above does not feature anything resembling a learning rate. Does this mean that the model always learns the same way? If so, how can we account for potential differences in learning across individuals? Perhaps, due to being a computational-level model, this approach is inadequate for describing how the data actually updates beliefs. However, we can still account for some individual variability by introducing different *inductive biases*, i.e., priors in the model. I envision the fitting process to be very computationally expensive, so an alternative and a crude way could be a very minimalistic grid search. We can simply compare several inductive biases for each subject and see which ones fit the data best. 

If we are not interested in estimating the individual differences, we can simply measure the goodness of fit between what the model predicts and the data (without maximizing this measure) and make conclusions about how people deviate from the ideal learner.

## Modeling choice
The model of learning relies on probabilistic concepts and thus contains quantities that can be linked to theoretical constructs, such as uncertainty and information-gain. It also lets us distinguish between the outcome uncertainty and the belief uncertainty. The outcome uncertainty is the uncertainty of prediction, given by $f(O \mid \boldsymbol\beta)$. The output of $f$ can be interpreted as the parameter of a Bernoulli distribution $p = f(O \mid \boldsymbol\beta)$, for which we can compute Entropy with $-p \log p$ or variance with $p(1-p)$, both of which peak at $p=0.5$. Thus, the output of $f$ allows us to quantify how uncertain the prediction that a monster prefers a certain food is.

The model also allows us to estimate belief uncertainty through parameter distributions. For example, if one is convinced that the base rate of liking a food is 0.5, one might represent the distribution of $\beta_0$ as very thinly dispersed around 0. Since we need to explicitly define the prior

As the learner makes more observations, these distributions change according to the Bayes rule. Differences between priors and posteriors indicate learning. We could look at information-gain, KL-divergence, and even the differences in outcome probabilities (i.e., confidence) and see which ones predict learnability ratings or choice better.

