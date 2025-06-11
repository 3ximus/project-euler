const N: usize = usize::pow(10, 10);

fn triangular(n: usize) -> usize {
    return n * (n + 1) / 2;
}
fn pentagonal(n: usize) -> usize {
    return n * (3 * n - 1) / 2;
}
fn hexagonal(n: usize) -> usize {
    return n * (2 * n - 1);
}

fn find(target: usize, index: usize, fun: fn(usize) -> usize) -> (bool, usize) {
    for i in index..N {
        let val = fun(i);
        if val == target {
            return (true, i);
        }
        if val > target {
            return (false, i);
        }
    }
    return (false, index);
}

fn main() {
    let mut ts_index = 1;
    let mut ps_index = 1;
    for i in 144..N {
        let h = hexagonal(i);
        let (found, new_p_index) = find(h, ps_index, pentagonal);
        ps_index = new_p_index;
        if found {
            let (found, new_j_index) = find(h, ts_index, triangular);
            ts_index = new_j_index;
            if found {
                println!("{h}");
                break;
            }
        }
    }
}
