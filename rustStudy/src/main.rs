fn add(a:i32,b:i32)->i32{
    return a+b;
}

fn main() {
    let mut number = 1;
    while number != 4 {
        println!("{}", number);
        number += 1;
    }
    println!("EXIT{}",add(7,8));
}