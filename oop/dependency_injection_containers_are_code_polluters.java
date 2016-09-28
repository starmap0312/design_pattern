// Dependency Injection Containers are Code Polluters
//
// example:
//
// (good design)

public class Budget {

    private final DB db;

    public Budget(DB data) { // dependency injection via constructor
        this.db = data;
    }

    public long total() {
        return this.db.cell("SELECT SUM(cost) FROM ledger");
    }
}

// the client code
public class App {

    public static void main(String... args) {

        Budget budget = new Budget(new Postgres("jdbc:postgresql:5740/main"));
        System.out.println("Total is: " + budget.total());
    }
}

// (bad design)

public class Budget {

    private final DB db = new Postgres("jdbc:postgresql:5740/main"); // a hidden/private knowledge/collaborator
    // class methods
}

// why is it bad?
// 1) code duplication
// 2) inability to reuse
// 3) inability to test

