import numpy as np
import yaml
import os
from src.logger import my_logger
from src.FrankWolfeVariants import awayStep_FW, blendedPairwise_FW, one_plus_eps_MEB_approximation
from src.utils import increment_path, load_config, generateRandomMatrix, plot_points_circle, fermat_spiral
from src.utils import create_save_dict, print_on_console, plot_graphs


# Change only this
yaml_name = "exp1.yaml"

# folder to load config file
config_path = "configs/"
# hyperparameters
config = load_config(yaml_name, config_path)
maxiter = eval(config.get('maxiter'))
epsilon = eval(config.get('epsilon'))
m = eval(config.get('number_of_samples'))
n = eval(config.get('number_of_variables'))
solver_methods = config.get('solver_methods')
data_creation_method = config.get('data_creation_method')
show_graphs = config.get('show_graphs')
test = config.get('test')

# TODO: solve MEB problem and find anomaly --points for Suleyman
# TODO: keep track of anomaly points --for Suleyman
# TODO: 2nd algoritm return negative and positive, check that it creates error --for Suleyman
# TODO: Add other line_search_strategies --for Suleyman
# TODO: do graphs and prints a helper function to get rid of messy codes
# TODO: check graphs lists of first and second algorithm

# TODO: find 2 datasets to check -- for Marija
# TODO: change size of active set in graph from float to int -- for Marija
# TODO: comparison graphs, check and write (with graph show, save) -- for Marija
# TODO: if you add any new graph function, you shold also call that graph function in plot graphs function
# in utils. I collected all graphs functions inside that.


if __name__ == '__main__':

    # Save path
    base_path = 'runs/'
    experiment_path = os.path.join(base_path, os.path.splitext(yaml_name)[0])
    # if there is an experiment with same experiment.yaml, increment_path_number exp1, exp2....
    incremented_path = increment_path(experiment_path, exist_ok=False, sep='_', mkdir=True)
    print(f"Results will be saved: {incremented_path}")

    logging = my_logger(incremented_path)

    logging.info("Creating data points")
    # Create Data
    if data_creation_method == "random":
        A = generateRandomMatrix(low=0, high=0.6, n=n, m=m)
        if test:
            T = generateRandomMatrix(low=0.7, high=1, n=n, m=m)
    elif data_creation_method == "fermat":
        A = fermat_spiral(m).T
    else:
        pass  # TODO: choose 2 datasets and add in this method

    #initialize YAML dicts
    asfw = {}
    bpfw = {}
    appfw = {}
    for method in solver_methods:

        if method == "asfw":
            print("\n*****************")
            title = "*  Away Step FW   *"
            print(title)
            print("*****************")

            logging.info("\nASFW algorithm started!")
            out_dict = awayStep_FW(A, epsilon, maxiter)

            # Print results:
            print_on_console(out_dict)

            # create dict to save results on YAML
            asfw = create_save_dict(out_dict)

            # Plot graphs for awayStep_FW
            graph_path = os.path.join(incremented_path, "asfw_graphs")
            plot_graphs(title,show_graphs,graph_path,out_dict)
            plot_points_circle(A, out_dict.get("radius"), out_dict.get("center"), title, graph_path, show_graphs)



        if method == "bpfw":
            print("\n*****************")
            title = "*  Blended Pairwise FW   *"
            print(title)
            print("*****************")

            logging.info("\nBPFW algorithm started!")
            out_dict = blendedPairwise_FW(A, epsilon, maxiter)
            # TODO: Debug - Here for dual_bp sometimes we get positive value, sometimes negative.

            # Print results:
            print_on_console(out_dict)

            # create dict to save results on YAML
            bpfw = create_save_dict(out_dict)

            # Plot graphs for blendedPairwise_FW
            graph_path = os.path.join(incremented_path, "bpfw_graphs")
            plot_graphs(title, show_graphs, graph_path, out_dict)
            plot_points_circle(A, out_dict.get("radius"), out_dict.get("center"), title, graph_path, show_graphs)


        if method == "appfw":
            print("\n*****************")
            title = "*  (1+epsilon)-approximation FW   *"
            print(title)
            print("*****************")
            logging.info("\n(1+epsilon)-approximation FW algorithm started!")

            out_dict = one_plus_eps_MEB_approximation(A, epsilon, maxiter)

            # Print results:
            print_on_console(out_dict)

            # create dict to save results on YAML
            appfw = create_save_dict(out_dict)

            # Plot graphs for one_plus_eps_MEB_approximation
            graph_path = os.path.join(incremented_path, "appfw_graphs")
            plot_graphs(title, show_graphs, graph_path, out_dict)
            plot_points_circle(A, out_dict.get("radius"), out_dict.get("center"), title, graph_path, show_graphs)


            # if test:
            #     # center
            #     # radius
            #     # test data
            #     graph_path = os.path.join(incremented_path, "test_graphs")
            #     os.mkdir(graph_path)
            #     plot_points_circle(T, radius_aproxAlg, center_aproxAlg, title, graph_path, show_graphs)
            #     true_positive = 0
            #     false_negative = 0
            #     for point_idx in range(m):
            #         dist = np.linalg.norm(T[:, point_idx] - center_aproxAlg)
            #         if dist > radius_aproxAlg:
            #             true_positive += 1
            #         else:
            #             false_negative += 1
            #     print(f"true poisitve {true_positive}/{(m)}")
            #     print(f"false negative {false_negative}/{m}")




    # Create yaml content
    output = {
        'config': config,
        'asfw': asfw,
        'bpfw': bpfw,
        'appfw': appfw,
    }

    # Save output yaml file
    with open(os.path.join(incremented_path, 'output.yaml'), 'w') as file:
        yaml.dump(output, file)
        logging.info(f"Output.yaml created")

