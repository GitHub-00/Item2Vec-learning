python=/usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6
user_rating_file='../data/ratings.csv'
train_file='../data/train_data.txt'
item_vec_file='../data/item_vec.txt'
item_sim_file='../data/sim_result.txt'

if [-f $user_rating_file]; then
    $python produce_train_data.py $user_train_file $train_file
else
    echo "no ratings file"
    exit
fi
if [-f $train_file]; then
    sh train.sh $train_file $item_vec_file
else
    echo "no train file"
    exit
fi
if [-f $item_vec]; then
    $python produce_item_sim.py $item_vec_file $item_sim_file
else
    echo "no item vec file"
    exit
fi

